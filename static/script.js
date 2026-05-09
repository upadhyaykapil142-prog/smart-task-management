const taskForm = document.getElementById("taskForm");
const taskList = document.getElementById("taskList");

// Fetch Tasks
async function fetchTasks() {

    const response = await fetch("/api/tasks");

    const tasks = await response.json();

    taskList.innerHTML = "";

    let completed = 0;

    tasks.forEach(task => {

        if (task.status === "Completed") {
            completed++;
        }

        const taskCard = document.createElement("div");

        taskCard.classList.add("task-card");

        taskCard.innerHTML = `
            <h3>${task.title}</h3>

            <p>${task.description}</p>

            <p><strong>Priority:</strong> ${task.priority}</p>

            <p><strong>Status:</strong> ${task.status}</p>

            <button class="complete-btn"
                onclick="completeTask(${task.id})">
                Complete
            </button>

            <button class="delete-btn"
                onclick="deleteTask(${task.id})">
                Delete
            </button>
        `;

        taskList.appendChild(taskCard);
    });

    // Analytics
    document.getElementById("totalTasks").innerText = tasks.length;

    document.getElementById("completedTasks").innerText = completed;

    document.getElementById("pendingTasks").innerText =
        tasks.length - completed;

    let percent = tasks.length === 0
        ? 0
        : ((completed / tasks.length) * 100).toFixed(1);

    document.getElementById("completionPercent").innerText =
        percent + "%";
}


// Add Task
taskForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    const taskData = {
        title: document.getElementById("title").value,

        description: document.getElementById("description").value,

        priority: document.getElementById("priority").value,

        status: document.getElementById("status").value
    };

    await fetch("/api/tasks", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(taskData)
    });

    taskForm.reset();

    fetchTasks();
});


// Delete Task
async function deleteTask(id) {

    await fetch(`/api/tasks/${id}`, {
        method: "DELETE"
    });

    fetchTasks();
}


// Complete Task
async function completeTask(id) {

    await fetch(`/api/tasks/${id}`, {

        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            status: "Completed"
        })
    });

    fetchTasks();
}


// Initial Fetch
fetchTasks();


// SocketIO Connection
const socket = io();

socket.on("task_update", function(data) {

    alert(data.message);

    fetchTasks();
});