import React from 'react'
import { Link } from 'react-router-dom'


export default function ProjectCard(props) {
    const data = props.data
    const arr = data.start_date.split('T')
    const arr2 = data.end_date.split('T')
    let crown = ''
    if (data.role == 'creator'){
      crown = <span role="img" aria-label="Crown">👑</span>
    }
  return (
    <div class="card text-center m-3">
  <div class="card-header">
    <h3>{data.role}{crown}</h3>
  </div>
  <div class="card-body">
    <h5 className="card-title" style={{fontSize:25}}>{data.name}</h5>
    <p className="card-text" style={{fontSize:17}}>{data.desc}</p>
    <Link to={`/project/${data.project_id}`} className="btn btn-primary">{data.project_id}</Link>
  </div>
  <div className="card-footer text-muted" style={{fontSize:20}}>
    Project period: from <b>{arr[0]}</b> to <b>{arr2[0]}</b>
  </div>
</div>
  )
}
