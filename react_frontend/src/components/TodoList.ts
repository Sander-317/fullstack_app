import React from "react";
import { useEffect, useState } from "react";

function TodoList() {
  const [data, setData] = useState([[]]);

  useEffect(() => {
    fetch("http://localhost:8000/todos")
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  console.log(data);

  const newArray = data.map((todo_text, index) => {
    return <li key={index}> {todo_text} </li>;
  });

  return newArray;
  // return "test todolist";
}

export default TodoList;
