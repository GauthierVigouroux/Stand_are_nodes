import { QueryResult } from "neo4j-driver";
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

    
    // on application exit:

app.post('/standard', (req, res) => {
  try{
    console.log("received request");
    let standard : Standard = req.body;
    dbReq.postStandard(standard).then((result : QueryResult)=>{
      console.log("result in  main :", result.summary.query.text);

    res.send(JSON.stringify(result))
    })
  }catch(err){
    res.status(500).send(err);

  }


})






