import { React, useEffect, useState } from "react";

export default function Test() {
  useEffect(() => {
    fetch("http://127.0.0.1:8000/test3");
  });

  return (
    <div>
      <div>
        <h2>Test</h2>
        <button onClick={() => console.log("test")}>add users</button>
      </div>
    </div>
  );
}
