import React from 'react'

class Users extends React.Component {
  constructor() {
    super()
    this.state = {selectOptionValue: "patrice"}
    this.handleOnChange = this.handleOnChange.bind(this)
  }

  handleOnChange(e) {
    console.log("change!")
    this.setState({
      selectOptionValue: e.target.value
    })
  }

  render() {
    const users = this.props.usersInfo.map(user => <option>{user}</option>)
    console.log('props', this.props)
    return(
      <div>
        <select class="form-control form-control-lg" onChange={this.handleOnChange}>
          {users}
        </select>
        <h3>Voici les films de <b>{this.state.selectOptionValue}</b></h3>
      </div>
    )
  }
}

export default Users
