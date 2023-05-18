import axios from 'axios';

const BASE_URL = 'http://localhost:5000';



class BackendApi {

  static async makeRequest(method, endpoint, token = null, data = {}) {
    try {
      const headers = { authorization: `Bearer ${token}` }
      // console.log(`${BASE_URL}${endpoint}`)
      return (
        await axios({ method, url: `${BASE_URL}${endpoint}`, data, headers })
      );
    } catch (err) {
      console.error(err);
    }
  }
    
  

  static async convert(formData) {
    const data = formData;
    return (
      await this.makeRequest('POST', '/convert', null, data)
    )
  }
}

export default BackendApi;