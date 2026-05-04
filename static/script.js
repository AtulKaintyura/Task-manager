const base = "http://127.0.0.1:5000";

async function signup() {
  await fetch(base + "/signup", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      name: name.value,
      email: email.value,
      password: password.value,
      role: role.value
    })
  });
  alert("Signup done");
  window.location.href = "/login-page";
}

async function login() {
  const res = await fetch(base + "/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      email: loginEmail.value,
      password: loginPassword.value
    })
  });

  const data = await res.json();

  if (res.status === 200) {
    window.location.href = "/dashboard-page";
  } else {
    alert(data.message);
  }
}

async function createProject() {
  await fetch(base + "/projects", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      name: projectName.value,
      created_by: createdBy.value
    })
  });
  alert("Project created");
}

async function createTask() {
  await fetch(base + "/tasks", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      title: taskTitle.value,
      status: taskStatus.value,
      project_id: projectId.value,
      assigned_to: assignedTo.value,
      deadline: deadline.value
    })
  });
  alert("Task created");
}

async function getTasks() {
  const res = await fetch(base + "/tasks");
  const data = await res.json();

  let rows = "";
  data.tasks.forEach(t => {
    rows += `<tr>
      <td>${t.id}</td>
      <td>${t.title}</td>
      <td>${t.status}</td>
    </tr>`;
  });

  taskTable.innerHTML = rows;
}

async function updateTask() {
  await fetch(base + "/tasks/" + taskId.value, {
    method: "PUT",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      status: newStatus.value
    })
  });
  alert("Updated");
}

async function loadDashboard() {
  const res = await fetch(base + "/dashboard");
  const data = await res.json();

  totalTasks.innerText = data.total_tasks;
  completedTasks.innerText = data.completed_tasks;
  pendingTasks.innerText = data.pending_tasks;
}