function getResponseFromAPI(){
promise.then (function(result)
{
    console.log(result);
})
promise.catch(function (error)
{
    console.log(error);
})
}