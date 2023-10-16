import { React, useState, useEffect } from "react";

export default function Todos() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/todos")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setTodos(data);
      });
  }, []);
  return (
    <div>
      <h2>Users</h2>
      {typeof todos === "undefined" ? (
        <p>loading...</p>
      ) : (
        todos.map((todo, i) => <p key={i}> {todo} </p>)
      )}
    </div>
  );
}
