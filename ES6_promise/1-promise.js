function getFullResponseFromAPI(success) {
    if (success) {
        resolve({ status: 200, body:'Success' });
    }
    else
        reject(Error('The fake API is not working currently'))
    return new Promise(resolve, reject)
   
}
export default getFullResponseFromAPI;
