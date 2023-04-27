import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import ProjectCard from './ProjectCard'

export default function UserProfile(props) {
    const navigate = useNavigate()
    const SignedID = props.SignedID
    if (SignedID ==''){
        navigate('/signin')
    }
    const [user, setUser] = useState({})
    const [projects, setProjects] = useState([])
    useEffect(()=>{
        fetch('http://localhost:5000/user/' + SignedID)
        .then(res => res.json())
        .then(data => {setUser(data)
             console.log(data)})
    },[])
    useEffect(()=>{
        fetch('http://localhost:5000/user/' + SignedID+'/projects')
        .then(res => res.json())
        .then(data => {setProjects(data)
        console.log(data)})
    },[])
    //console.log(SignedID)
  return (
    <>
    <div className="container-fluid mt-5">
        <div className="row bg-primary">
            <div className="col-12">
                <h1 className='text-center'>Welcome {user.name}</h1>
            </div>
        </div>
    </div>
    <div className="container-fluid p-3">
        <div className="row">
            <div className="col-md-6 bg-primary">
                <h1 className='text-center'>Your Projects</h1>
                {projects.map((project)=>
                {return <ProjectCard data={project}></ProjectCard>}
                )}
            </div>
            <div className="col-md-6 bg-info">
                <h1 className='text-center'>Your Tasks</h1>
            </div>
        </div>
    </div>
    </>
    
    
  )
}
