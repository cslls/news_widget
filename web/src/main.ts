import "./style.css";
// import axios from "axios";

const targetUrl = "http://localhost:8000/api/news";
fetch(targetUrl)
  .then((response) => response.json())
  .then((data) => console.log(data));

// axios
//   .get("http://localhost:8000/api/news")
//   .then((response) => {
//     console.log(response.data);
//   })
//   .catch((error) => {
//     console.log(error);
//   });

document.querySelector<HTMLDivElement>("#app")!.innerHTML = `
  <div>
    hello world
  </div>
`;
