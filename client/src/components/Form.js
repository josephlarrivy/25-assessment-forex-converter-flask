import React, { useEffect, useState } from "react";
import BackendApi from "../api/BackendApi";



const Form = () => {

  const [data, setData] = useState()

  const getCurrencies = async () => {
    const response = await BackendApi.getSuppotredCurrencies()
    // console.log(response)
    let currencies = response.data.data;
    for (let key in currencies) {
      let currency = currencies[key];
      console.log(`Currency Code: ${currency.code}`);
      console.log(`Currency Description: ${currency.description}`);
    }
  }

  useEffect(() => {
    getCurrencies()
  }, [])

  useEffect(() => {
    console.log(data)
  }, [data])

  return (
    <div>

    </div>
  )
}

export default Form;