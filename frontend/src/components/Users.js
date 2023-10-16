import { React, useEffect, useState } from "react";

export default function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/test2")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setUsers(data);
      });
  }, []);
  return (
    <div>
      <h2>Users</h2>
      {typeof users === "undefined" ? (
        <p>loading...</p>
      ) : (
        users.map((user, i) => <p key={i}> {user} </p>)
      )}
    </div>
  );
}
