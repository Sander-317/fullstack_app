import { React, useEffect, useState } from "react";

export default function Test() {
  const [data, setData] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/test")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setData(data);
      });
  }, []);

  return (
    <div>
      <h1>test</h1>
      {data.map((i) => {
        return <div> {i}</div>;
      })}
    </div>
  );
}
