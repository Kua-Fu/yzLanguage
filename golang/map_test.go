package main

import (
	"fmt"
	"testing"
)

func TestMap(t *testing.T) {

	s := map[string]string{
		"1": "11",
	}
	f1, ok := s["1"]
	f2, f2OK := s["2"]
	fmt.Println("f1, ok", f1, ok)
	fmt.Println("f2, ok", f2, f2OK)
}
