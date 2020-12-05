import React from 'react'

function Main() {
  const date = new Date()
  const hours = date.getHours()
  let timeOfDay

  let styles = {
    color:'red',
  }

  if(hours < 12) {
    timeOfDay = 'morning'
    styles.color = 'blue'
  } else {
    timeOfDay = 'afternoon'
  }

  return(
    <main style={styles}>Good {timeOfDay}!</main>
  )
}

export default Main
