package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
)

func main() {
    file, err := ioutil.ReadFile("./jsonFile.json")
    if err != nil {
        panic(err)
    }

    var data interface{}
    err = json.Unmarshal(file, &data)
    if err != nil {
        panic(err)
    }

    root := data.(map[string]interface{})
    key1 := root["key1"].(string)
    fmt.Println(key1)
    key2 := root["key2"].(map[string]interface{})
    fmt.Println(key2)
    key3 := root["key3"].([]interface{})
    value3 := key3[0].(string)
    fmt.Println(value3)
}
