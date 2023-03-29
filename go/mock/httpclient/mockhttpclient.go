package mock

import (
    "bytes"
    "fmt"
    "io"
    "net/http"
)

type MockHttpClient struct {
    Req       *http.Request
    Responses []*http.Response
    Err       error
}

func NewMockHttpClient() *MockHttpClient {
    return &MockHttpClient{}
}

func (m *MockHttpClient) QueueResponse(status int, body string) {
    res := http.Response{
        Status:        fmt.Sprintf("%d", status),
        StatusCode:    status,
        Proto:         "HTTP/1.1",
        ProtoMajor:    1,
        ProtoMinor:    1,
        Body:          io.NopCloser(bytes.NewBufferString(body)),
        ContentLength: int64(len(body)),
        Request:       nil,
        Header:        make(http.Header, 0),
    }
    m.Responses = append(m.Responses, &res)
}

func (m *MockHttpClient) ReturnWithError(err error) {
    m.Err = err
}

func (m *MockHttpClient) Do(req *http.Request) (*http.Response, error) {
    m.Req = req

    if m.Err != nil {
        return nil, m.Err
    }

    res := m.Responses[0]
    m.Responses = m.Responses[1:]
    return res, nil
}

func (m *MockHttpClient) InspectRequestBody() string {
    body, err := io.ReadAll(m.Req.Body)
    if err != nil {
        panic("bad requst body")
    }
    return string(body)
}
