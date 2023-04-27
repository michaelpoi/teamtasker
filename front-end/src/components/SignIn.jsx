import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'

export default function SignIn(props) {
    const setID = props.setID
    const navigate = useNavigate()
    const [login, setLogin] = useState('')
    const [password, setPassword] = useState('')
    const [data,setData] = useState({})
    const handleSubmit = async (e) =>{
      console.log(login)
        e.preventDefault()
          try {
            // Send username and password to backend for authentication
            const response = await fetch('http://localhost:5000/user/signin', {
              method: 'POST',
              body: JSON.stringify({ login, password }),
              headers: { 'Content-Type': 'application/json' },
            });
            const ans = await response.json()
            //console.log(ans)
            if (ans.authenticated !== false) {
              // User is authenticated, perform further actions
              console.log('Sign-in successful!');
              setID(ans)
              navigate('/profile')
            } else {
              // Authentication failed, handle error
              console.error('Sign-in failed:', response.statusText);
            }
          } catch (error) {
            console.error('Error during sign-in:', error);
          }
        };
  return (
    <div className="container mt-5">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="login">Login</label>
            <input type="text" className="form-control" id="login" name="login" value={login} onChange={(e) => setLogin(e.target.value)}/>
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input type="password" className="form-control" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
          </div>
          <button type="submit" className="btn btn-primary mt-3" onClick={handleSubmit}>Submit</button>
        </form>
    </div>
  )
}

