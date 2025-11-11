import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import axios from 'axios';
import { Product } from './productSlice';
import { logout } from './authSlice';

interface WishlistState {
  items: Product[];
  loading: boolean;
  error: string | null;
  wishlistStatus: Record<number, boolean>; // productId -> isInWishlist
}

const initialState: WishlistState = {
  items: [],
  loading: false,
  error: null,
  wishlistStatus: {},
};

const API_BASE_URL = 'http://localhost:8080/api';

// Get authorization header from token
const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

// Fetch user's wishlist
export const fetchWishlist = createAsyncThunk(
  'wishlist/fetchWishlist',
  async (_, { rejectWithValue }) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/wishlist`, {
        headers: getAuthHeaders(),
      });
      return response.data;
    } catch (error: any) {
      if (error.response?.status === 401) {
        return rejectWithValue('Please login to view your wishlist');
      }
      return rejectWithValue(error.response?.data?.error || 'Failed to fetch wishlist');
    }
  }
);

// Add product to wishlist
export const addToWishlist = createAsyncThunk(
  'wishlist/addToWishlist',
  async (productId: number, { rejectWithValue }) => {
    try {
      const response = await axios.post(
        `${API_BASE_URL}/wishlist/add/${productId}`,
        {},
        { headers: getAuthHeaders() }
      );
      return { productId, message: response.data.message };
    } catch (error: any) {
      if (error.response?.status === 401) {
        return rejectWithValue('Please login to add items to wishlist');
      }
      return rejectWithValue(error.response?.data?.error || 'Failed to add to wishlist');
    }
  }
);

// Remove product from wishlist
export const removeFromWishlist = createAsyncThunk(
  'wishlist/removeFromWishlist',
  async (productId: number, { rejectWithValue }) => {
    try {
      await axios.delete(`${API_BASE_URL}/wishlist/remove/${productId}`, {
        headers: getAuthHeaders(),
      });
      return productId;
    } catch (error: any) {
      if (error.response?.status === 401) {
        return rejectWithValue('Please login to remove items from wishlist');
      }
      return rejectWithValue(error.response?.data?.error || 'Failed to remove from wishlist');
    }
  }
);

// Check if product is in wishlist
export const checkWishlistStatus = createAsyncThunk(
  'wishlist/checkWishlistStatus',
  async (productId: number, { rejectWithValue }) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/wishlist/check/${productId}`, {
        headers: getAuthHeaders(),
      });
      return { productId, isInWishlist: response.data.isInWishlist };
    } catch (error: any) {
      // If not authenticated, return false
      return { productId, isInWishlist: false };
    }
  }
);

const wishlistSlice = createSlice({
  name: 'wishlist',
  initialState,
  reducers: {
    clearWishlist: (state) => {
      state.items = [];
      state.wishlistStatus = {};
    },
    updateWishlistStatus: (state, action: PayloadAction<{ productId: number; isInWishlist: boolean }>) => {
      state.wishlistStatus[action.payload.productId] = action.payload.isInWishlist;
    },
  },
  extraReducers: (builder) => {
    builder
      // Fetch wishlist
      .addCase(fetchWishlist.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchWishlist.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
        // Update wishlist status for all items
        action.payload.forEach((product: Product) => {
          state.wishlistStatus[product.id] = true;
        });
      })
      .addCase(fetchWishlist.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      // Add to wishlist
      .addCase(addToWishlist.fulfilled, (state, action) => {
        state.wishlistStatus[action.payload.productId] = true;
      })
      // Remove from wishlist
      .addCase(removeFromWishlist.fulfilled, (state, action) => {
        state.wishlistStatus[action.payload] = false;
        state.items = state.items.filter((item) => item.id !== action.payload);
      })
      // Check wishlist status
      .addCase(checkWishlistStatus.fulfilled, (state, action) => {
        state.wishlistStatus[action.payload.productId] = action.payload.isInWishlist;
      })
      // Clear wishlist when user logs out
      .addCase(logout, (state) => {
        state.items = [];
        state.wishlistStatus = {};
        state.error = null;
      });
  },
});

export const { clearWishlist, updateWishlistStatus } = wishlistSlice.actions;
export default wishlistSlice.reducer;

