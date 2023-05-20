import React, { useEffect, useState } from "react";
import BackendApi from "../api/BackendApi";
import '../styles/Form.css'

const Form = () => {
  const [data, setData] = useState([]);
  const [fromInput, setFromInput] = useState("");
  const [toInput, setToInput] = useState("");
  const [amountInput, setAmountInput] = useState("")
  const [output, setOutput] = useState()

  const getCurrencies = async () => {
    try {
      const response = await BackendApi.getSuppotredCurrencies();
      const currencies = response.data.data;
      const array = Object.keys(currencies).map((key) => {
        const currency = currencies[key];
        return {
          code: currency.code,
          name: currency.description
        };
      });
      setData(array);
    } catch (error) {
      console.log("Error fetching currencies:", error);
    }
  };


  useEffect(() => {
    getCurrencies();
    console.log(data)
  }, []);

  const handleFromInputChange = (event) => {
    setFromInput(event.target.value);
  };

  const handleToInputChange = (event) => {
    setToInput(event.target.value);
  };

  const handleAmountInputChange = (event) => {
    setAmountInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(fromInput, toInput, amountInput);

    const response = await BackendApi.convert({
      'from' : fromInput,
      'to' : toInput,
      'amount' : amountInput
    })

    console.log(response.data)
    setOutput(response.data)
    setAmountInput('')


  };

  return (
    <div id="main-container">
      <form onSubmit={handleSubmit} id='form'>
        <p>Select a 'from' currency, a 'to' currency, and enter and amount.</p>
        <hr></hr>
        <label htmlFor="from">From</label>
        <br></br>
        <select id="from" value={fromInput} onChange={handleFromInputChange}>
          <option value="">Select a currency</option>
          {data.map((currency) => (
            <option key={currency.code} value={currency.code}>
              {currency.name}
            </option>
          ))}
        </select>
        <br></br>
        <br></br>
        <label htmlFor="to">To</label>
        <br></br>
        <select id="to" value={toInput} onChange={handleToInputChange}>
          <option value="">Select a currency</option>
          {data.map((currency) => (
            <option key={currency.code} value={currency.code}>
              {currency.name}
            </option>
          ))}
        </select>
        <br></br>
        <br></br>
        <label htmlFor="to">Amount</label>
        <br></br>
        <input
          type="number"
          id="to"
          value={amountInput}
          onChange={handleAmountInputChange}
        />
        <br></br>
        <br></br>
        <button type="submit">Submit</button>
      </form>
      <br></br>
      {output && 
        <div id="output">
          <p>{output.amount} {output.from} = {output.result} {output.to}</p>
        </div>
      }
    </div>
  );
};

export default Form;
