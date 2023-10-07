import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("http://localhost:8000/test")
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      {typeof data.test === "undefined" ? (
        <p>loading</p>
      ) : (
        data.test.map((test, i) => <p key={i}>{test}</p>)
      )}
    </div>
  );
}

export default App;
