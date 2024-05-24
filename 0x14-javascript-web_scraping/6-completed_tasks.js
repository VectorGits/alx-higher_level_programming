#!/usr/bin/node
// computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];


request(url, (err, response, body) => {
    if (err) {
        console.error(err);
        
    } else {
        const tasks = JSON.parse(body);
        const completedTasks = {};

        for (const task of tasks) {
            if (task.completed) {
                if (task.userId in completedTasks) {
                    completedTasks[task.userId]++;
                } else {
                    completedTasks[task.userId] = 1;
                }
            }
        }
    }
    console.log(completedTasks);
});
