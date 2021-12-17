package main

import (
	"encoding/json"
	"fmt"
	"testing"
)

func TestLongString(t *testing.T) {
	s := `
111
222
333
`
	fmt.Println("s---", s)
}

type Info struct {
	A map[string]string `json:"a"`
	// B string `json:"b"`
}

func TestSliceIndex(t *testing.T) {
	s := []string{"1", "2", "3"}
	s1 := s[0:1]
	fmt.Println("s1---", s1)
}

func TestJson(t *testing.T) {
	info := map[string]interface{}{
		"a": map[string]string{"1": "11"},
		"b": "2",
	}
	strInfo, _ := json.Marshal(info)
	fmt.Println("---str--", string(strInfo))
	var msg Info
	err := json.Unmarshal(strInfo, &msg)
	fmt.Println("err--", err)
	fmt.Println("s--", msg)
}

func TestMarshal(t *testing.T) {
	d := map[string]interface{}{
		"a": "11",
		"b": "22",
	}
	fmt.Println("ori d --", d)
	dm, _ := json.Marshal(d)
	var res map[string]interface{}
	json.Unmarshal(dm, &res)
	fmt.Printf("%T, %v", res["a"], res["a"])

}

func TestStringType(t *testing.T) {
	s := map[string]interface{}{
		"1": "11",
		"2": 22,
	}
	f1, ok := s["1"].(string)
	f2, f2ok := s["2"].(string)
	f3, f3ok := s["3"].(string)
	fmt.Println("f1, f1ok--", f1, ok)
	fmt.Println("f2, f2ok--", f2, f2ok)
	fmt.Println("f3, f3ok--", f3, f3ok)
}
