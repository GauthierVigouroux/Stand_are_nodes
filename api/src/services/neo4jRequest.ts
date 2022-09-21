import { QueryResult, Session } from "neo4j-driver";
import { Standard } from "../modeles/interfaces/standard";
import { QueryJson } from "../modeles/interfaces/queryJson";
import { json } from "stream/consumers";
import axios from "axios";
import https from "https";

function queryDb(queryJson : QueryJson, session: Session) : Promise<any>{
  
    return new  Promise(async (res, reject) => {        
        //     console.log("1");

        //    axios.post("neo4j+s://d195505e.databases.neo4j.io:7687", JSON.stringify(queryJson)).then((result)=>{
        //     console.log("2");
        //     res(result);
        //    }).catch((err) => {
        //     console.log("3");
        //     console.log(err);
        //     throw(err)

        // });

        

        const options = {
            hostname: 'neo4j+s://d195505e.databases.neo4j.io',
            port : '7687',
            path: '/db/data/transaction/commit',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        };
        
        
        const req = https.request(options, (res) => {
            let data = '';
        
            console.log('Status Code:', res.statusCode);
        
            res.on('data', (chunk) => {
                data += chunk;
            });
        
            res.on('end', () => {
                console.log('Body: ', JSON.parse(data));
            });
        
        }).on("error", (err) => {
            console.log("Error: ", err.message);
        });
        
        req.write(JSON.stringify(queryJson));
        req.end();
    }
}

export function postStandard(standard : Standard, session: Session) : Promise<QueryResult>{

    let queryJson = new QueryJson();
    
    queryJson.statement.push({statement : `MERGE (referedNode : Standard { name : "${standard.name}"})`})

    //We create all node referenced if they do not exist yet and create a relationShip with them 
    standard.references.forEach((referedStandard : Standard)=>{
        //Create refered node 
        // queryJson.statement.push({statement : `MERGE (referedNode : Standard { name : "${referedStandard.name}"})`})
        // queryJson.statement.push({statement : `MERGE (mainNode : Standard { name : "${standard.name}"})-[r:REFERENCES]->(referedNode : Standard { name : "${referedStandard.name}"})`})
        //Create relationShip between the main node and the refered node 
    })
    console.log("query : ", JSON.stringify(queryJson));
    return queryDb(queryJson, session);
}
