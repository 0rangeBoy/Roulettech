import './App.css';
import { React, useEffect, useCallback } from 'react';
import Header from "./components/Header";
import { Grid, TextField, Button } from "@mui/material/";
import axios from "axios";


function test1 = () => {

const textData = useCallback(async () => {
  const d1 = await axios.get('/apiText/pApp/').then(response => response.data);



}, [])
}

const imgData = useCallback(async () => {
  const d2 = await axios.get('/apiImg/pApp/').then(response => response.data);
}, [])

function App() {



 (async () => {
    console.log(await textData())
    console.log(await imgData())
 })()



  return (
  
    <div className="App">
      <Header />
      <div className="apibox" id="textbox">
        <h3>
          Text Storage
        </h3>
        <div className="storageBox">
        <ul>

        </ul>
          </div>
          <div className="inputBox">
            <Grid container spacing={0}>
                <Grid item xs={12}>
                  <TextField name ='text' fullWidth label="Enter Text" variant="outlined" id="textInput" InputProps={{endAdornment:<Button id ="textButton" variant="text">Insert</Button>}}/>
                </Grid>
              </Grid>
          </div>
        </div>
        <div className="apibox" id="imgbox">
        <h3>
         Image Storage
        </h3>
            <div className="storageBox">
            <ul>
              </ul>
            </div>
            <div className="inputBox">
              <Grid container spacing={0}>
                <Grid item xs={12}>
                  <TextField name = 'img' fullWidth label="Enter Image URL" variant="outlined" id="imageInput" InputProps={{endAdornment:<Button variant="text">Insert</Button>}}/>
                </Grid>
              </Grid>
            </div>
        </div>
    </div>
  );
}
export default App;
