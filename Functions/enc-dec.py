import numpy as np

class EncoderDecoderLSTM:
    def __init__(self, input_size, hidden_size, output_size, num_layers):
        # Initialize model parameters
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.num_layers = num_layers
        
        # Initialize LSTM weights
        self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wo = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wy = np.random.randn(output_size, hidden_size)
        
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))
        self.bc = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def forward(self, x):
        T = x.shape[0] # Length of input sequence
        h = np.zeros((self.hidden_size, 1)) # Initialize hidden state
        c = np.zeros((self.hidden_size, 1)) # Initialize cell state
        hs = [] # Hidden states
        cs = [] # Cell states
        
        # Encoder LSTM forward pass
        for t in range(T):
            xt = x[t].reshape((-1, 1)) # Reshape input vector
            ft = self.sigmoid(np.dot(self.Wf, np.concatenate((h, xt))) + self.bf)
            it = self.sigmoid(np.dot(self.Wi, np.concatenate((h, xt))) + self.bi)
            ot = self.sigmoid(np.dot(self.Wo, np.concatenate((h, xt))) + self.bo)
            ct_hat = np.tanh(np.dot(self.Wc, np.concatenate((h, xt))) + self.bc)
            c = ft * c + it * ct_hat
            h = ot * np.tanh(c)
            hs.append(h)
            cs.append(c)
            
        # Decoder LSTM forward pass
        y = np.zeros((T, self.output_size)) # Initialize output sequence
        h = hs[-1] # Set decoder initial hidden state to encoder final hidden state
        c = cs[-1] # Set decoder initial cell state to encoder final cell state
        
        for t in range(T):
            yt_hat = np.dot(self.Wy, h) + self.by
            y[t] = yt_hat.ravel() # Flatten output vector
            yt = y[t].reshape((-1, 1)) # Reshape output vector
            it = self.sigmoid(np.dot(self.Wi, np.concatenate((h, yt))) + self.bi)
            ot = self.sigmoid(np.dot(self.Wo, np.concatenate((h, yt))) + self.bo)
            ct_hat = np.tanh(np.dot(self.Wc, np.concatenate((h, yt))) + self.bc)
            c = it * ct_hat + (1 - it) * c
            h = ot * np.tanh(c)
            
        return y
        
    def backward(self, x, y, lr=0.01):
        T = x.shape[0] # Length of input sequence
        dh_next = np.zeros((self.hidden_size, 1)) # Initialize decoder next hidden state
