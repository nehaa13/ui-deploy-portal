const API = "http://backend-url";

async function loadLOBs() {
  const res = await fetch(`${API}/lobs`);
  const lobs = await res.json();
  fill("lob", lobs);
}

async function loadEnvs() {
  const lob = value("lob");
  const res = await fetch(`${API}/envs?lob=${lob}`);
  fill("env", await res.json());
}

async function loadPackages() {
  const lob = value("lob");
  const env = value("env");
  const res = await fetch(`${API}/packages?lob=${lob}&env=${env}`);
  fill("package", await res.json());
}

async function loadServers() {
  const lob = value("lob");
  const env = value("env");
  const res = await fetch(`${API}/servers?lob=${lob}&env=${env}`);
  fill("servers", await res.json());
}

async function deploy() {
  const body = {
    lob: value("lob"),
    env: value("env"),
    package: value("package"),
    servers: selected("servers")
  };

  await fetch(`${API}/deploy`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(body)
  });

  alert("Deployment triggered");
}
