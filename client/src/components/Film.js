import React from 'react'
// import { Card, Button, Text } from 'react-native'
//
// const Film = () => {
//   return (
//   <Card style={{ width: '18rem' }}>
//     <Card.Img variant="top" src="./images/film1.jpg/100px180" />
//     <Card.Body>
//       <Card.Title>Card Title</Card.Title>
//         <Card.Text>
//           Some quick example text to build on the card title and make up the bulk of
//           the card's content.
//         </Card.Text>
//       <Button variant="primary">Go somewhere</Button>
//     </Card.Body>
//   </Card>
//   )
// }

function Film(props){
  return(
    <div class="col">
      <div class="card" style={{width: 15 + 'rem'}} >
        <img class="card-img-top" src={props.filmInfo.imgUrl} alt="Card image cap"/>
        <div class="card-body">
          <h5 class="card-title">{props.filmInfo.title}</h5>
          <p class="card-text">Année de sortie: {props.filmInfo.year}</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>
    </div>
  )
}

export default Film
