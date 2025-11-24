import axios from 'axios';
import { store } from '../store/store';
import { restoreAuth, logout } from '../store/slices/authSlice';

// Configure axios defaults
axios.defaults.baseURL = 'http://localhost:8080/api';

// Request interceptor to add auth token to all requests
axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle 401 errors globally
axios.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;

    // If we get a 401 and haven't already tried to restore auth
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      const token = localStorage.getItem('token');
      
      // Only try to restore auth if we have a token
      if (token) {
        try {
          // Try to restore authentication - this is critical to get user object
          const result = await store.dispatch(restoreAuth());
          
          // Update the authorization header with the token
          const newToken = localStorage.getItem('token');
          if (newToken && originalRequest.headers) {
            originalRequest.headers.Authorization = `Bearer ${newToken}`;
          }
          
          // Always retry the request after restore attempt
          // If restore succeeded, we have user. If it failed, we still have token
          return axios(originalRequest);
        } catch (authError) {
          // If auth restoration fails, still retry with existing token
          console.error('Auth restoration error in interceptor:', authError);
          if (originalRequest.headers) {
            originalRequest.headers.Authorization = `Bearer ${token}`;
          }
          return axios(originalRequest);
        }
      }
    }

    return Promise.reject(error);
  }
);

export default axios;

