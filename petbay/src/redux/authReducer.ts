import { createSlice } from '@reduxjs/toolkit';

export interface AuthState {
    isAuthenticated: boolean | null; 
  }
  
  const initialState: AuthState = {
    isAuthenticated: false,
  };
  
  const authSlice = createSlice({
    name: 'auth',
    initialState: initialState,
    reducers: {
      loginUser: (state) => {
        state.isAuthenticated = true;
      },
      logoutUser: (state) => {
        state.isAuthenticated = false;
      },
    },
  });
  
  export const { loginUser, logoutUser } = authSlice.actions;

  export default authSlice.reducer;