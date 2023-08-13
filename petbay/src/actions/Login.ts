import { LoginUser } from "../models/auth/User";

export const handleUserLogin = async (user: LoginUser) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
      });
  
      if (response.ok) {
        const data = await response.json();
        return data;
      } else {
        const errorData = await response.json();
        throw new Error(errorData.error); 
        return null;
      }
    } catch (error:any) {
      throw new Error(error.message);
    }
  };
  