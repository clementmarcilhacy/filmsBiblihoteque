import React from 'react'

class LoggInOut extends React.Component {
  constructor() {
    super()
    this.state = {loggedIn : true}
    this.handleClick = this.handleClick.bind(this)
  }

  handleClick() {
    console.log(this.state)
    this.setState(prevState => {
      return {loggedIn : !prevState.loggedIn}
    })
  }

  render() {
    return(
      <div>
        <h1>Your are logged {this.state.loggedIn ? 'In' : 'Out'}</h1>
        <button class="btn btn-primary" onClick={this.handleClick}>Logg In/Out</button>
      </div>
    )
  }
}

export default LoggInOut
