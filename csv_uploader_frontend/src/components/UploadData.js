import axios from "axios";
import React, { useState, useRef } from "react";
import { baseURL } from "../services/backend.service";
import { usePapaParse } from 'react-papaparse';
import { cityToState } from "./CityToState";

export const UploadData = () => {
    const inputFile = useRef(null);
    const { readString } = usePapaParse();
    const [csvFile, setCsvFile] = useState(null);

    const handleChange = (event) => {
        setCsvFile(event.target.files[0]);
    };
    
    const uploadCSV = () => {
        readString(csvFile, {
            header: true,
            complete: (results) => {
                results.data.forEach(upload)
            }
        })
    };

    function upload(data) {
        var first_name = "", middle_name = "", last_name = "", state = "", school = "", classes = [];
        for(let key in data) {
            if (key.toUpperCase() === "FIRST NAME" || key.toUpperCase() === "NAME") {
                first_name = data[key]
            } else if(key.toUpperCase() === "MIDDLE NAME") {
                middle_name = data[key]
            } else if(key.toUpperCase() === "LAST NAME") {
                last_name = data[key]
            } else if(key.toUpperCase() === "STATE" || key.toUpperCase() === "LOCATION") {
                state = cityToState[data[key]]
            } else if(key.toUpperCase() === "SCHOOL") {
                school = data[key]
            } else if(key.toUpperCase().includes("CLASS")) {
                if (data[key] !== null && data[key] !== "") {
                    classes.push(data[key])
                }
            }
        }
        for(let i in classes) {
            let data_object = {
                Name: first_name + " " + middle_name + " " + last_name,
                Class: classes[i],
                School: school,
                State: state
            }
            axios.post(`${baseURL}/csv_uploader_api/`, data_object)
            .then((response) => {
                console.log("Success")
                console.log(response.data)
            }).catch((e) => {
                console.log("Failure")
                console.log(e)
            })
        }
    };

    return (
        <div className="submit-form">
            <h2>Import CSV File!</h2>
            <input className="csv-input" type="file" accept=".csv" required
                ref={inputFile}
                name="fileInput"
                onInput={handleChange}
            />
            <p />
            <button onClick={uploadCSV}>Upload now!</button>
        </div>
    );
}

export default UploadData;