import React, { useEffect } from 'react'
import BackendApi from '../api/BackendApi'


const ApiTestingComponent = () => {


  const makeRequest = async () => {
    console.log('test')
    const request = await BackendApi.convert(
      {
        'from' : 'USD',
        'to' : 'EUR',
        'amount' : '1200'
      }
    )
    console.log(request)
  } 


  useEffect(() => {
    makeRequest()
  }, [])



  return (
    <div>

    </div>
  )
}

export default ApiTestingComponent;