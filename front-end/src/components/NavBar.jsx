import React from 'react'
import {Link} from "react-router-dom"

export default function NavBar() {
  return (
    <nav className='navbar fixed-top navbar-expand-lg'>
        <a className='navbar-brand' href='#'>TeamTasker</a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className='navbar-nav ms-auto'>
            <Link
             to = {'/'}
             className = "nav-link"
            >
                Home
            </Link>
            <Link
             to={'/signup'}
             className='nav-link'>
                Sign Up
             </Link>
        </ul>
      </div>
    </nav>
  )
}
