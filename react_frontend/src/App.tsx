import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("http://localhost:8000/test2")
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
      {typeof data === "undefined" ? (
        <p>loading</p>
      ) : (
        data.map((test, i) => <p key={i}>{test}</p>)
      )}
    </div>
  );
}

export default App;
