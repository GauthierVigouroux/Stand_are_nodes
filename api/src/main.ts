import { QueryResult } from "neo4j-driver";
import express, { Response } from "express";
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

/**
 * Function use to globalize the management of the service's response. 
 * Allows to consequently reduce the size of the code by making the same function execute the response made 
 * by the services queries
 * 
 * @param resSource The object containing the logic used to answer the http request made to the api
 * @param serviceFunction the function of the service that we are waiting an answer from
 */

function serviceRequest(resSource : Response, serviceFunction : Promise<any>){

  try{
    serviceFunction.then((result : QueryResult)=>{
      console.log("result in  main :", result.summary.query.text);

      resSource.send(JSON.stringify(result))
    })
  }catch(err){
    resSource.status(500).send(err);

  }
}

/**
 * Endpoint to insert a node (THE MAIN NODE ), nodes the MAIN NODE has relationship with (THE REFERED NODES) and the relationShip between the MAIN NODE and each of the REFERED NODES 
 */
app.post('/standard', (req, res) => {
  let standard : Standard = req.body;
  serviceRequest(res, dbReq.postStandard(standard))
})

/**
 *  endpoint to delete all node in the database, thus deleting all relationShips existing as well
 */
app.delete('/standards', (req, res) => {
  serviceRequest(res, dbReq.deleteAll())
})






