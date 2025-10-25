// Пример данных
var groupmates = [
    {name: 'Иван', surname: 'Иванов', group: 'Б9123', marks: [4, 4, 5, 5, 4]},
    {name: 'Петр', surname: 'Петров', group: 'Б9124', marks: [3, 2, 3, 4, 3]},
    {name: 'Сергей', surname: 'Сергеев', group: 'Б9123', marks: [5, 5, 5, 5, 5]},
    {name: 'Anastasia', surname: 'Romanova', group: 'Б9125', marks: [5, 4, 3, 4, 5]},
    {name: 'Aleksei', surname: 'Smirnov', group: 'Б9123', marks: [3, 3, 4, 2, 4]},
    {name: 'Мария', surname: 'Кузнецова', group: 'Б9124', marks: [4, 4, 4, 5, 4]},
    {name: 'Елена', surname: 'Васильева', group: 'Б9140', marks: [5, 5, 5, 5, 4]},
    {name: 'John', surname: 'Smith', group: 'Б9140', marks: [2, 3, 4, 3, 2]},
    {name: 'Дмитрий', surname: 'Фёдоров', group: 'Б9125', marks: [4, 2, 3, 4, 5]},
    {name: 'Olga', surname: 'Ivanova', group: 'Б9123', marks: [5, 5, 4, 4, 5]},
    {name: 'Ли', surname: 'Чен', group: 'Б9124', marks: [3, 2, 3, 2, 4]},
    {name: 'Игорь', surname: 'Соколов', group: 'Б9123', marks: [4, 3, 4, 4, 4]},
    {name: 'Анна', surname: 'Лебедева', group: 'Б9125', marks: [3, 4, 5, 5, 5]},
    {name: 'Sophia', surname: 'Brown', group: 'Б9140', marks: [5, 4, 4, 4, 3]},
    {name: 'Егор', surname: 'Воробьев', group: 'Б9123', marks: [4, 4, 5, 4, 5]}
];


// Фильтрация по средней оценке
function filterByAverageMark(students, minAvg) {
    var filtered = [];
    for (var i = 0; i < students.length; i++) {
        var marks = students[i]['marks'];
        var avg = marks.reduce((a, b) => a + b, 0) / marks.length;
        if (avg > minAvg) {
            filtered.push(students[i]);
        }
    }
    return filtered;
}

// Генерация HTML-таблицы для студентов
function renderStudents(students) {
    var resultDiv = document.querySelector('.students-result');
    if (students.length === 0) {
        resultDiv.innerHTML = "<b>Нет студентов с таким средним баллом.</b>";
        return;
    }
    var html = '<table><tr><th>Имя</th><th>Фамилия</th><th>Группа</th><th>Оценки</th></tr>';
    for (var i = 0; i < students.length; i++) {
        html += '<tr>' +
            '<td>' + students[i]['name'] + '</td>' +
            '<td>' + students[i]['surname'] + '</td>' +
            '<td>' + students[i]['group'] + '</td>' +
            '<td>' + students[i]['marks'].join(", ") + '</td>' +
            '</tr>';
    }
    html += '</table>';
    resultDiv.innerHTML = html;
}

// Обработчик кнопки фильтрации
function showFilteredStudents() {
    var minAvg = parseFloat(document.getElementById('minAverage').value);
    var filtered = filterByAverageMark(groupmates, minAvg);
    renderStudents(filtered);
}
