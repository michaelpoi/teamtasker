import React from 'react'

export default function TaskCard(props) {
    const data = props.data
  return (
    <div className="card">
  <div className="card-header">
    <h5 className="card-title">{data.name}</h5>
    <p className="card-text">{data.end_date}</p>
  </div>
  <div className="card-body">
    <p className="card-text">{data.desc}</p>
    <div className="form-check">
      <input type="checkbox" className="form-check-input" id="isDoneCheckbox"/>
      <label className="form-check-label" htmlFor="isDoneCheckbox">Is Done</label>
    </div>
    <p className="card-text"><small className="text-muted">{data.role}</small></p>
  </div>
</div>
  )
}
