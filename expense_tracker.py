<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expense Tracker</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #chart {
            width: 800px;
            height: 400px;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Expense Tracker</a>
    </nav>
    <div class="container mt-5">
        <h1>Expenses</h1>
        <table id="expenses-table" class="table table-striped">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Category</th>
                    <th>Amount</th>
                    <th>Description</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody id="expenses-body">
            </tbody>
        </table>
        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#add-expense-modal">Add Expense</button>
        <button type="button" class="btn btn-secondary" id="view-chart-btn">View Chart</button>
        <div id="chart" style="display: none;"></div>
    </div>

    <!-- Add Expense Modal -->
    <div class="modal fade" id="add-expense-modal" tabindex="-1" role="dialog" aria-labelledby="add-expense-modal-label" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="add-expense-modal-label">Add Expense</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form id="add-expense-form">
                        <div class="form-group">
                            <label for="date">Date</label>
                            <input type="date" class="form-control" id="date" required>
                        </div>
                        <div class="form-group">
                            <label for="category">Category</label>
                            <select class="form-control" id="category" required>
                                <option value="">Select Category</option>
                                <option value="Food">Food</option>
                                <option value="Transportation">Transportation</option>
                                <option value="Entertainment">Entertainment</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="amount">Amount</label>
                            <input type="number" class="form-control" id="amount" required>
                        </div>
                        <div class="form-group">
                            <label for="description">Description</label>
                            <textarea class="form-control" id="description" required></textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="add-expense-btn">Add Expense</button>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.8.0/dist/chart.min.js"></script>
    <script>
        let expenses = [];

        $(document).ready(function() {
            $("#add-expense-btn").click(function() {
                addExpense();
            });
            $("#view-chart-btn").click(function() {
                viewChart();
            });
        });

        function addExpense() {
            let expense = {
                date: $("#date").val(),
                category: $("#category").val(),
                amount: $("#amount").val(),
                description: $("#description").val()
            };
            expenses.push(expense);
            updateExpensesTable();
            $("#add-expense-modal").modal("hide");
            $("#add-expense-form")[0].reset();
        }

        function updateExpensesTable() {
            let tbody = $("#expenses-body");
            tbody.empty();
            for (let i = 0; i < expenses.length; i++) {
                let expense = expenses[i];
                let row = "<tr>";
                row += "<td>" + expense.date + "</td>";
                row += "<td>" + expense.category + "</td>";
                row += "<td>" + expense.amount + "</td>";
                row += "<td>" + expense.description + "</td>";
                row += "<td><button class='btn btn-danger' onclick='deleteExpense(" + i + ")'>Delete</button></td>";
                row += "</tr>";
                tbody.append(row);
            }
        }

        function deleteExpense(index) {
            expenses.splice(index, 1);
            updateExpensesTable();
        }

        function viewChart() {
            let ctx = document.getElementById("chart").getContext("2d");
            let chart = new Chart(ctx, {
                type: "bar",
                data: {
                    labels: expenses.map(expense => expense.date),
                    datasets: [{
                        label: "Expenses",
                        data: expenses.map(expense => expense.amount),
                        backgroundColor: "rgba(255, 99, 132, 0.2)",
                        borderColor: "rgba(255, 99, 132, 1)",
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
            $("#chart").show();
        }
    </script>
</body>
</html>
