import { useState } from "react";
import { LoginUser } from "../../models/auth/User";
import { handleUserLogin } from "../../actions/Login";
import { loginUser } from '../../redux/authReducer';

import "../../assets/css/Login.scss"
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";

const Login = ()=> {
    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');

    const navigate = useNavigate()
    const dispatch = useDispatch(); 

    const handleLogin = async () => {

        const user : LoginUser = {email:email,password:password}

        try {
          const response: any = await handleUserLogin(user);
          console.log("Response is : ", response)
          if (response) {
            dispatch(loginUser()); 
            return navigate("/home")
          }
        } catch (error:any) {
          console.error('Login failed:', error.message);
        }
      };

    return(
        <>
         <div className="login">
            <div className="inner">
            <h1>Login</h1>
            <label className="form-label"  htmlFor="username">UserName | Email</label>
            <input
                type="text"
                name="username"
                placeholder="Username"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="form-control"
            />
            <label className="form-label" htmlFor="password">Password</label>
            <input
                type="password"
                name="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="form-control"
            />
            <button 
                onClick={handleLogin}
                className="btn btn-primary"
                style={{marginTop:'10px'}}
            >
                Login
            </button>
            </div>
    </div>
        </>
    );
}


export default Login;


