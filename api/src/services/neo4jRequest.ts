import { Standard } from "../modeles/interfaces/standard";
import db, { QueryResult, Session } from "neo4j-driver";

const dbUri = "neo4j+s://d195505e.databases.neo4j.io:7687/db/data/transaction/commit" 
const user = "neo4j" 
const password = "HjIJGZdNmrRc_4twhYSbZW0XF4qOmiMVNwuYCejIIww" 


const driver = db.driver(dbUri, db.auth.basic(user, password))


/**
 * interface used to query statements to the neo4j database
 */
type QueryStatement = {
    query : string, 
    parameters : Object
}

/**
 * Query a list of statements to the db
 * @param queryStatements list of query statements
 * @returns 
 */
function queryDb(queryStatements : QueryStatement[]) : Promise<any>{
    return new  Promise(async (res, reject) => {  
        const session = driver.session()

        try{
            let result;
            for(const queryStatement of queryStatements){
                result = await session.run(queryStatement.query, queryStatement.parameters);
            }
            res(result);

        }catch(error){
            console.log(error);
            reject(error)
        }
        session.close();

    })
}

/**
 * //create a Standard and its relationship with other standards, create the other standards if they do not exist yet
 * //3 queries are made one after the other : 
 *  1) create the main standard if it doesn't exist yet
 *  2) create the other standards referenced b the main standard if they do not exit
 *  3) create the relationships between the main node and the reffered standards
 * @param standard the main Standard to createe
 * @returns 
 */
export function postStandard(standard : Standard) : Promise<QueryResult>{

    return new Promise<QueryResult>( (res, reject)=>{
        
        //queries building
        let mainNodeId = "mainNode";
        let secondNodeId = "referedNode";

        let firstNode = `(${mainNodeId}: Standard { name : $mainNodeName})`
        let secondNode = `(${secondNodeId} : Standard { name : $referedNodeName})`

        let mergeFirstNodeQuery = `MERGE ${firstNode}`;
        let mergeSecondNodeQuery = `MERGE ${secondNode}`;
        let relationShipQuery = `MATCH ${firstNode}, ${secondNode} merge (${mainNodeId})-[r:REFERENCES]->(${secondNodeId})`;

        try{
            //statements building
            let queryStatements : QueryStatement[] = [];
            queryStatements.push({query : mergeFirstNodeQuery, parameters : {mainNodeName : standard.name}})
            for (const referedStandard of standard.references) {
                queryStatements.push({query : mergeSecondNodeQuery, parameters : {referedNodeName : referedStandard.name}})
                queryStatements.push({query : relationShipQuery, parameters : {mainNodeName : standard.name, referedNodeName : referedStandard.name}})
            }

            //results of the last of the 3 queries
            let result = queryDb(queryStatements);
            res(result)
        }
        catch(error){
            reject(error)
        }
    })
}

/**
 * delete all the nodes in the database
 * @returns the result of the delete query
 */
export function deleteAll(){
    let query = "MATCH(n) DETACH DELETE n ";
    let queryStatements : QueryStatement[] = [];
    queryStatements.push({query : query, parameters : {}})
    let result = queryDb(queryStatements);
    return result
}