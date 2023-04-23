import {React, useState} from 'react'
//import {useHistory} from 'react-router-dom'


export default function SignUp() {
    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [login, setLogin] = useState('')
    const [password, setPassword] = useState('')
    const [user, setUser] = useState({})
    //const history = useHistory()
    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = {name, email, login, password};
        const response = await fetch('http://localhost:5000/user/', {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify(data)
        })
        console.log(user)
        console.log(response)
        console.log(JSON.stringify(data))
        if (response.ok){
            console.log('Response worked')
        }
        console.log('Form submitted:', { name, email, login, password });
      };
  return (
    <div className="container mt-5">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="name">Name</label>
            <input type="text" className="form-control" id="name" name="name" value={name} onChange={(e) => setName(e.target.value)}/>
          </div>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input type="email" className="form-control" id="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)}/>
          </div>
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
