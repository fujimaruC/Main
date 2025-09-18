from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime
import math

app = Flask(__name__)

class TaskManager:
    def __init__(self):
        self.tasks_file = 'tasks.json'
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        else:
            # Sample tasks for demo
            sample_tasks = [
                {
                    "id": 1,
                    "text": "Design modern UI components",
                    "completed": False,
                    "created_at": "2024-01-15T10:00:00"
                },
                {
                    "id": 2,
                    "text": "Implement smooth animations",
                    "completed": True,
                    "created_at": "2024-01-14T14:30:00"
                },
                {
                    "id": 3,
                    "text": "Create responsive layout",
                    "completed": False,
                    "created_at": "2024-01-13T09:15:00"
                },
                {
                    "id": 4,
                    "text": "Add glassmorphism effects",
                    "completed": False,
                    "created_at": "2024-01-12T16:45:00"
                },
                {
                    "id": 5,
                    "text": "Test user experience flow",
                    "completed": True,
                    "created_at": "2024-01-11T11:20:00"
                },
                {
                    "id": 6,
                    "text": "Deploy to production server",
                    "completed": False,
                    "created_at": "2024-01-10T08:30:00"
                },
                {
                    "id": 7,
                    "text": "Write documentation",
                    "completed": False,
                    "created_at": "2024-01-09T15:20:00"
                },
                {
                    "id": 8,
                    "text": "Setup continuous integration",
                    "completed": True,
                    "created_at": "2024-01-08T12:45:00"
                }
            ]
            self.save_tasks(sample_tasks)
            return sample_tasks
    
    def save_tasks(self, tasks=None):
        if tasks is None:
            tasks = self.tasks
        try:
            with open(self.tasks_file, 'w') as f:
                json.dump(tasks, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, text):
        new_id = max([task['id'] for task in self.tasks], default=0) + 1
        task = {
            "id": new_id,
            "text": text,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.tasks.insert(0, task)
        self.save_tasks()
        return task
    
    def toggle_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                break
        self.save_tasks()
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
    
    def get_filtered_tasks(self, filter_type="all", search=""):
        filtered = self.tasks.copy()
        
        if filter_type == "active":
            filtered = [task for task in filtered if not task["completed"]]
        elif filter_type == "completed":
            filtered = [task for task in filtered if task["completed"]]
        
        if search:
            filtered = [task for task in filtered if search.lower() in task["text"].lower()]
        
        return filtered
    
    def get_stats(self):
        total = len(self.tasks)
        completed = len([task for task in self.tasks if task["completed"]])
        active = total - completed
        return {"total": total, "completed": completed, "active": active}

# Initialize task manager
task_manager = TaskManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks')
def get_tasks():
    filter_type = request.args.get('filter', 'all')
    search = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 6))
    
    filtered_tasks = task_manager.get_filtered_tasks(filter_type, search)
    total_tasks = len(filtered_tasks)
    total_pages = math.ceil(total_tasks / per_page) if total_tasks > 0 else 1
    
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_tasks = filtered_tasks[start_idx:end_idx]
    
    return jsonify({
        'tasks': paginated_tasks,
        'total_tasks': total_tasks,
        'total_pages': total_pages,
        'current_page': page,
        'stats': task_manager.get_stats()
    })

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or not data.get('text', '').strip():
        return jsonify({'error': 'Task text is required'}), 400
    
    task = task_manager.add_task(data['text'].strip())
    return jsonify({'task': task, 'stats': task_manager.get_stats()})

@app.route('/api/tasks/<int:task_id>/toggle', methods=['PUT'])
def toggle_task(task_id):
    task_manager.toggle_task(task_id)
    return jsonify({'stats': task_manager.get_stats()})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return jsonify({'stats': task_manager.get_stats()})

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Create the HTML template
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TaskFlow - Modern Task Manager</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .glass {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .task-card {
            transition: all 0.3s ease;
        }
        .task-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }
        .btn-modern {
            background: linear-gradient(45deg, #667eea, #764ba2);
            transition: all 0.3s ease;
        }
        .btn-modern:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        .fade-in {
            animation: fadeIn 0.5s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .stat-card {
            background: linear-gradient(45deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255,255,255,0.2);
            transition: all 0.3s ease;
        }
        .stat-card:hover {
            transform: translateY(-5px);
            background: linear-gradient(45deg, rgba(255,255,255,0.15), rgba(255,255,255,0.1));
        }
    </style>
</head>
<body class="min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <div class="max-w-6xl mx-auto">
            <!-- Header -->
            <div class="text-center mb-12">
                <h1 class="text-6xl font-bold text-white mb-4 drop-shadow-lg">
                    <i class="fas fa-tasks mr-4"></i>TaskFlow
                </h1>
                <p class="text-xl text-white/80">Fluid, Modern Task Management</p>
            </div>

            <!-- Stats Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8" id="statsContainer">
                <!-- Stats will be loaded here -->
            </div>

            <!-- Main Task Panel -->
            <div class="glass rounded-3xl shadow-2xl overflow-hidden">
                <!-- Controls -->
                <div class="p-8 border-b border-white/20">
                    <!-- Add Task -->
                    <div class="flex gap-4 mb-6">
                        <input 
                            type="text" 
                            id="newTaskInput"
                            placeholder="What needs to be done today?"
                            class="flex-1 bg-white/10 border border-white/20 rounded-2xl px-6 py-4 text-white placeholder-white/60 focus:outline-none focus:ring-2 focus:ring-white/50 focus:border-transparent transition-all duration-300"
                        >
                        <button 
                            onclick="addTask()"
                            class="btn-modern text-white px-8 py-4 rounded-2xl font-semibold flex items-center gap-2"
                        >
                            <i class="fas fa-plus"></i>
                            Add Task
                        </button>
                    </div>

                    <!-- Search and Filters -->
                    <div class="flex flex-col md:flex-row gap-4">
                        <div class="flex-1 relative">
                            <i class="fas fa-search absolute left-4 top-1/2 transform -translate-y-1/2 text-white/60"></i>
                            <input 
                                type="text" 
                                id="searchInput"
                                placeholder="Search tasks..."
                                class="w-full bg-white/10 border border-white/20 rounded-xl pl-12 pr-6 py-3 text-white placeholder-white/60 focus:outline-none focus:ring-2 focus:ring-white/50 transition-all duration-300"
                                oninput="searchTasks()"
                            >
                        </div>
                        <div class="flex gap-2">
                            <button onclick="setFilter('all')" class="filter-btn px-6 py-3 rounded-xl font-medium transition-all duration-300 bg-white/20 text-white hover:bg-white/30" data-filter="all">
                                All
                            </button>
                            <button onclick="setFilter('active')" class="filter-btn px-6 py-3 rounded-xl font-medium transition-all duration-300 bg-white/10 text-white/80 hover:bg-white/20" data-filter="active">
                                Active
                            </button>
                            <button onclick="setFilter('completed')" class="filter-btn px-6 py-3 rounded-xl font-medium transition-all duration-300 bg-white/10 text-white/80 hover:bg-white/20" data-filter="completed">
                                Completed
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Tasks List -->
                <div class="p-8" id="tasksContainer">
                    <!-- Tasks will be loaded here -->
                </div>

                <!-- Pagination -->
                <div class="p-8 border-t border-white/20" id="paginationContainer">
                    <!-- Pagination will be loaded here -->
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentFilter = 'all';
        let currentSearch = '';
        let currentPage = 1;

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            loadTasks();
            
            // Add Enter key support for new task input
            document.getElementById('newTaskInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    addTask();
                }
            });
        });

        async function loadTasks() {
            try {
                const response = await fetch(`/api/tasks?filter=${currentFilter}&search=${encodeURIComponent(currentSearch)}&page=${currentPage}`);
                const data = await response.json();
                
                displayTasks(data.tasks);
                updateStats(data.stats);
                updatePagination(data);
            } catch (error) {
                console.error('Error loading tasks:', error);
            }
        }

        function displayTasks(tasks) {
            const container = document.getElementById('tasksContainer');
            
            if (tasks.length === 0) {
                container.innerHTML = `
                    <div class="text-center py-16">
                        <i class="fas fa-tasks text-6xl text-white/30 mb-4"></i>
                        <p class="text-white/60 text-xl">No tasks found</p>
                        <p class="text-white/40 text-sm mt-2">Try adjusting your search or filter</p>
                    </div>
                `;
                return;
            }

            container.innerHTML = tasks.map((task, index) => `
                <div class="task-card bg-white/5 hover:bg-white/10 rounded-2xl p-6 mb-4 border border-white/10 hover:border-white/20 fade-in" style="animation-delay: ${index * 100}ms">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-4 flex-1">
                            <button 
                                onclick="toggleTask(${task.id})"
                                class="w-6 h-6 rounded-full border-2 transition-all duration-300 flex items-center justify-center ${task.completed ? 'bg-green-500 border-green-500 text-white' : 'border-white/50 hover:border-green-400 hover:bg-green-400/10'}"
                            >
                                ${task.completed ? '<i class="fas fa-check text-xs"></i>' : ''}
                            </button>
                            <div class="flex-1">
                                <p class="text-lg transition-all duration-300 ${task.completed ? 'text-white/50 line-through' : 'text-white'}">
                                    ${task.text}
                                </p>
                                <p class="text-white/40 text-sm mt-1">
                                    <i class="far fa-calendar-alt mr-1"></i>
                                    Created ${formatDate(task.created_at)}
                                </p>
                            </div>
                        </div>
                        <button 
                            onclick="deleteTask(${task.id})"
                            class="text-red-400 hover:text-red-300 p-3 hover:bg-red-500/10 rounded-xl transition-all duration-300"
                        >
                            <i class="fas fa-trash-alt"></i>
                        </button>
                    </div>
                </div>
            `).join('');
        }

        function updateStats(stats) {
            const container = document.getElementById('statsContainer');
            container.innerHTML = `
                <div class="stat-card rounded-2xl p-6">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-white/60 text-sm mb-1">Total Tasks</p>
                            <p class="text-3xl font-bold text-white">${stats.total}</p>
                        </div>
                        <div class="bg-blue-500/20 rounded-full p-3">
                            <i class="fas fa-list-ul text-blue-300 text-xl"></i>
                        </div>
                    </div>
                </div>
                <div class="stat-card rounded-2xl p-6">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-white/60 text-sm mb-1">Completed</p>
                            <p class="text-3xl font-bold text-white">${stats.completed}</p>
                        </div>
                        <div class="bg-green-500/20 rounded-full p-3">
                            <i class="fas fa-check-circle text-green-300 text-xl"></i>
                        </div>
                    </div>
                </div>
                <div class="stat-card rounded-2xl p-6">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-white/60 text-sm mb-1">Active</p>
                            <p class="text-3xl font-bold text-white">${stats.active}</p>
                        </div>
                        <div class="bg-purple-500/20 rounded-full p-3">
                            <i class="fas fa-clock text-purple-300 text-xl"></i>
                        </div>
                    </div>
                </div>
            `;
        }

        function updatePagination(data) {
            const container = document.getElementById('paginationContainer');
            
            if (data.total_pages <= 1) {
                container.style.display = 'none';
                return;
            }
            
            container.style.display = 'block';
            
            const startItem = (data.current_page - 1) * 6 + 1;
            const endItem = Math.min(data.current_page * 6, data.total_tasks);
            
            container.innerHTML = `
                <div class="flex items-center justify-between">
                    <div class="text-white/60 text-sm">
                        Showing ${startItem} to ${endItem} of ${data.total_tasks} tasks
                    </div>
                    <div class="flex items-center gap-2">
                        <button 
                            onclick="changePage(${data.current_page - 1})" 
                            ${data.current_page === 1 ? 'disabled' : ''}
                            class="p-2 rounded-lg bg-white/10 text-white hover:bg-white/20 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-300"
                        >
                            <i class="fas fa-chevron-left"></i>
                        </button>
                        ${Array.from({length: data.total_pages}, (_, i) => i + 1).map(num => `
                            <button 
                                onclick="changePage(${num})"
                                class="px-4 py-2 rounded-lg font-medium transition-all duration-300 ${num === data.current_page ? 'bg-white/20 text-white' : 'bg-white/5 text-white/70 hover:bg-white/10 hover:text-white'}"
                            >
                                ${num}
                            </button>
                        `).join('')}
                        <button 
                            onclick="changePage(${data.current_page + 1})" 
                            ${data.current_page === data.total_pages ? 'disabled' : ''}
                            class="p-2 rounded-lg bg-white/10 text-white hover:bg-white/20 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-300"
                        >
                            <i class="fas fa-chevron-right"></i>
                        </button>
                    </div>
                </div>
            `;
        }

        async function addTask() {
            const input = document.getElementById('newTaskInput');
            const text = input.value.trim();
            
            if (!text) {
                alert('Please enter a task!');
                return;
            }

            try {
                const response = await fetch('/api/tasks', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text: text })
                });

                if (response.ok) {
                    input.value = '';
                    currentPage = 1; // Reset to first page
                    loadTasks();
                } else {
                    alert('Error adding task');
                }
            } catch (error) {
                console.error('Error adding task:', error);
                alert('Error adding task');
            }
        }

        async function toggleTask(id) {
            try {
                const response = await fetch(`/api/tasks/${id}/toggle`, {
                    method: 'PUT'
                });

                if (response.ok) {
                    loadTasks();
                }
            } catch (error) {
                console.error('Error toggling task:', error);
            }
        }

        async function deleteTask(id) {
            if (!confirm('Are you sure you want to delete this task?')) {
                return;
            }

            try {
                const response = await fetch(`/api/tasks/${id}`, {
                    method: 'DELETE'
                });

                if (response.ok) {
                    loadTasks();
                }
            } catch (error) {
                console.error('Error deleting task:', error);
            }
        }

        function setFilter(filter) {
            currentFilter = filter;
            currentPage = 1;
            
            // Update filter button appearances
            document.querySelectorAll('.filter-btn').forEach(btn => {
                if (btn.dataset.filter === filter) {
                    btn.className = 'filter-btn px-6 py-3 rounded-xl font-medium transition-all duration-300 bg-white/20 text-white';
                } else {
                    btn.className = 'filter-btn px-6 py-3 rounded-xl font-medium transition-all duration-300 bg-white/10 text-white/80 hover:bg-white/20';
                }
            });
            
            loadTasks();
        }

        function searchTasks() {
            currentSearch = document.getElementById('searchInput').value;
            currentPage = 1;
            loadTasks();
        }

        function changePage(page) {
            currentPage = page;
            loadTasks();
        }

        function formatDate(dateString) {
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', {
                month: 'short',
                day: 'numeric',
                year: 'numeric'
            });
        }
    </script>
</body>
</html>'''
    
    with open('templates/index.html', 'w') as f:
        f.write(html_template)
    
    print("🚀 TaskFlow Server Starting...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("✨ Modern, fluid design - tidak kaku lagi!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
