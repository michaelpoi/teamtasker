import React, { useEffect, useState } from 'react'
import { useNavigate} from 'react-router-dom'
import ProjectCard from './ProjectCard'
import TaskCard from './TaskCard'

export default function UserProfile(props) {
    const navigate = useNavigate()
    const SignedID = props.SignedID
    if (SignedID ==''){
        navigate('/signin')
        console.log('idi nahui')
    }
    const [user, setUser] = useState({})
    const [projects, setProjects] = useState([])
    const [tasks, setTasks] = useState([])
    useEffect(()=>{
        if(SignedID != ''){
            fetch('http://localhost:5000/user/' + SignedID)
        .then(res => res.json())
        .then(data => {setUser(data)
             console.log(data)})
        }
        else{
            navigate('/signin')
        }
    },[])
    useEffect(()=>{
        fetch('http://localhost:5000/user/' + SignedID+'/projects')
        .then(res => res.json())
        .then(data => {setProjects(data)
        console.log(data)})
    },[])
    useEffect(()=>{
        fetch('http://localhost:5000/user/' + SignedID+'/tasks')
        .then(res =>res.json())
        .then(data =>setTasks(data))
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
                {return <ProjectCard data={project} key={project.id}></ProjectCard>}
                )}
            </div>
            <div className="col-md-6 bg-info">
                <h1 className='text-center'>Your Tasks</h1>
                {tasks.map((task)=>
                {return <TaskCard data={task} key={task.task_id}></TaskCard>}
                )}
            </div>
        </div>
    </div>
    </>
    
    
  )
}
