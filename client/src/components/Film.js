import React from 'react'

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
