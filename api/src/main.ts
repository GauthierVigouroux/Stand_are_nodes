import db, { QueryResult } from "neo4j-driver";
import express from "express";
import { Standard } from "./modeles/interfaces/standard";
import * as dbReq from "./services/neo4jRequest";



const serverPort  = 8080;

const app = express();
app.use(express.json());

app.use(function(req, res, next) {
  res.setHeader("Content-Type", "application/json");
  next();
});

app.listen(serverPort);

console.log("server started on :", serverPort)

const dbUri = "neo4j+s://d195505e.databases.neo4j.io:7687/db/data/transaction/commit" 
const user = "neo4j" 
const password = "HjIJGZdNmrRc_4twhYSbZW0XF4qOmiMVNwuYCejIIww" 

const driver = db.driver(dbUri, db.auth.basic(user, password))
const session = driver.session()


    
    // on application exit:

app.post('/standard', (req, res) => {
  try{
    console.log("received request");
    let standard : Standard = req.body;
    dbReq.postStandard(standard, session).then((result : QueryResult)=>{
    res.write(JSON.stringify(result));
    })
  }catch(err){
    res.status(500).send(err);

  }


})

//do something when app is closing
// process.on('exit', exitHandler.bind(null,{cleanup:true}, driver, session));






