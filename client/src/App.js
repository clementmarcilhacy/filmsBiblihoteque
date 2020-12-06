import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Navbar from './components/Navbar'
import Main from './components/Main'
import Users from './components/Users'
import Film from './components/Film'
import LoggInOut from './components/LoggInOut'

const users = ['patrice', 'armelle', 'jules', 'felix', 'sophie', 'clement']

const App = props => {
  useEffect(() => {
    axios.get('/api/hello')
    .then(res => setState(res.data))
  }, [])

  const [state, setState] = useState('')

  console.log(state)
  const films = Object.keys(state).map(key => < Film key={key} filmInfo={{title:state[key].title, year:state[key].year, imgUrl:state[key].imgUrl}}/>)

  console.log(users)
  return(
    <div>
      < Navbar />
        <br/>
        < LoggInOut />
        <br/>
        < Users usersInfo={users}/>
        <br/>
        <div class="row">
          {films}
        </div>
    </div>
  )
}

export default App
