<script lang="ts">
  import { onMount } from 'svelte';
  import {
    checkBackendStatus,
    startRecording,
    stopRecording,
    transcribeAudio,
    type TranscriptionResponse,
  } from '$lib/api';

  // State variables
  let isRecording = $state(false);
  let isTranscribing = $state(false);
  let backendStatus = $state('checking');
  let transcription = $state<TranscriptionResponse | null>(null);
  let errorMessage = $state('');

  // Check if the backend is running when the component mounts
  onMount(async () => {
    try {
      const status = await checkBackendStatus();
      backendStatus = status.status;
    } catch (error) {
      backendStatus = 'error';
      errorMessage =
        'Failed to connect to the backend. Make sure it is running.';
    }
  });

  // Start recording audio
  async function handleStartRecording() {
    try {
      errorMessage = '';
      const result = await startRecording();

      if (result.file) {
        isRecording = true;
      } else {
        errorMessage = result.message;
      }
    } catch (error) {
      errorMessage = `Failed to start recording: ${error}`;
    }
  }

  // Stop recording and optionally transcribe
  async function handleStopRecording(transcribe = false) {
    try {
      if (!isRecording) return;

      const result = await stopRecording();
      isRecording = false;

      if (transcribe && result.file) {
        await handleTranscribe();
      }
    } catch (error) {
      errorMessage = `Failed to stop recording: ${error}`;
    }
  }

  // Transcribe the recorded audio
  async function handleTranscribe() {
    try {
      isTranscribing = true;
      errorMessage = '';
      transcription = await transcribeAudio();

      if (!transcription.success) {
        errorMessage = transcription.error || 'Transcription failed';
      }
    } catch (error) {
      errorMessage = `Failed to transcribe audio: ${error}`;
    } finally {
      isTranscribing = false;
    }
  }

  // Format time in seconds to MM:SS format
  function formatTime(seconds: number): string {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
  }
</script>

<main class="container">
  <h1>Audio Transcription with Whisper.cpp</h1>

  <!-- Backend Status -->
  <div class="status-container">
    <div
      class="status-indicator {backendStatus === 'ready'
        ? 'status-ready'
        : 'status-error'}"
    ></div>
    <span
      >Backend Status: {backendStatus === 'ready'
        ? 'Connected'
        : 'Not Connected'}</span
    >
  </div>

  <!-- Error Message -->
  {#if errorMessage}
    <div class="error-message">
      {errorMessage}
    </div>
  {/if}

  <!-- Recording Controls -->
  <div class="controls">
    {#if !isRecording}
      <button
        class="record-button"
        onclick={handleStartRecording}
        disabled={backendStatus !== 'ready' || isTranscribing}
      >
        Start Recording
      </button>
    {:else}
      <button class="stop-button" onclick={() => handleStopRecording(false)}>
        Stop Recording
      </button>
      <button
        class="transcribe-button"
        onclick={() => handleStopRecording(true)}
      >
        Stop & Transcribe
      </button>
    {/if}

    {#if !isRecording && !isTranscribing && backendStatus === 'ready'}
      <button
        class="transcribe-button"
        onclick={handleTranscribe}
        disabled={isTranscribing}
      >
        Transcribe Last Recording
      </button>
    {/if}
  </div>

  <!-- Recording Indicator -->
  {#if isRecording}
    <div class="recording-indicator">
      <div class="recording-pulse"></div>
      <span>Recording...</span>
    </div>
  {/if}

  <!-- Transcribing Indicator -->
  {#if isTranscribing}
    <div class="transcribing-indicator">
      <div class="spinner"></div>
      <span>Transcribing...</span>
    </div>
  {/if}

  <!-- Transcription Results -->
  {#if transcription && transcription.success}
    <div class="transcription-container">
      <h2>Transcription</h2>

      <div class="transcription-text">
        {transcription.text}
      </div>

      {#if transcription.segments && transcription.segments.length > 0}
        <h3>Segments</h3>
        <div class="segments-container">
          {#each transcription.segments as segment}
            <div class="segment">
              <div class="segment-time">
                [{formatTime(segment.start)} → {formatTime(segment.end)}]
              </div>
              <div class="segment-text">
                {segment.text}
              </div>
            </div>
          {/each}
        </div>
      {/if}
    </div>
  {/if}
</main>

<style>
  :root {
    font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 24px;
    font-weight: 400;
    color: #0f0f0f;
    background-color: #f6f6f6;
    font-synthesis: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    -webkit-text-size-adjust: 100%;
  }

  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    display: flex;
    flex-direction: column;
  }

  h1 {
    font-size: 2rem;
    margin-bottom: 1.5rem;
    color: #333;
    text-align: center;
  }

  h2 {
    font-size: 1.5rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
    color: #333;
  }

  h3 {
    font-size: 1.2rem;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
    color: #555;
  }

  .status-container {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
  }

  .status-indicator {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-right: 0.5rem;
  }

  .status-ready {
    background-color: #4caf50;
  }

  .status-error {
    background-color: #f44336;
  }

  .error-message {
    background-color: #ffebee;
    color: #d32f2f;
    padding: 0.75rem;
    border-radius: 4px;
    margin-bottom: 1rem;
    border-left: 4px solid #d32f2f;
  }

  .controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
    justify-content: center;
  }

  button {
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 4px;
    font-weight: 600;
    cursor: pointer;
    transition:
      background-color 0.2s,
      transform 0.1s;
    font-family: inherit;
  }

  button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  button:active:not(:disabled) {
    transform: scale(0.98);
  }

  .record-button {
    background-color: #4caf50;
    color: white;
  }

  .record-button:hover:not(:disabled) {
    background-color: #43a047;
  }

  .stop-button {
    background-color: #f44336;
    color: white;
  }

  .stop-button:hover:not(:disabled) {
    background-color: #e53935;
  }

  .transcribe-button {
    background-color: #2196f3;
    color: white;
  }

  .transcribe-button:hover:not(:disabled) {
    background-color: #1e88e5;
  }

  .recording-indicator,
  .transcribing-indicator {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    justify-content: center;
  }

  .recording-pulse {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: #f44336;
    margin-right: 0.5rem;
    animation: pulse 1.5s infinite;
  }

  @keyframes pulse {
    0% {
      transform: scale(0.95);
      box-shadow: 0 0 0 0 rgba(244, 67, 54, 0.7);
    }

    70% {
      transform: scale(1);
      box-shadow: 0 0 0 10px rgba(244, 67, 54, 0);
    }

    100% {
      transform: scale(0.95);
      box-shadow: 0 0 0 0 rgba(244, 67, 54, 0);
    }
  }

  .spinner {
    width: 16px;
    height: 16px;
    border: 2px solid #ccc;
    border-top-color: #2196f3;
    border-radius: 50%;
    margin-right: 0.5rem;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  .transcription-container {
    background-color: #f5f5f5;
    padding: 1.5rem;
    border-radius: 8px;
    margin-top: 1.5rem;
  }

  .transcription-text {
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
    white-space: pre-wrap;
  }

  .segments-container {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    max-height: 400px;
    overflow-y: auto;
    padding-right: 0.5rem;
  }

  .segment {
    display: flex;
    flex-direction: column;
    padding: 0.75rem;
    background-color: white;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  }

  .segment-time {
    font-size: 0.85rem;
    color: #757575;
    margin-bottom: 0.25rem;
    font-family: monospace;
  }

  .segment-text {
    font-size: 1rem;
    line-height: 1.5;
  }

  /* Responsive adjustments */
  @media (max-width: 600px) {
    .container {
      padding: 1rem;
    }

    .controls {
      flex-direction: column;
      gap: 0.75rem;
    }

    button {
      width: 100%;
    }
  }

  @media (prefers-color-scheme: dark) {
    :root {
      color: #f6f6f6;
      background-color: #2f2f2f;
    }

    .transcription-container {
      background-color: #3f3f3f;
    }

    .segment {
      background-color: #2f2f2f;
    }

    .error-message {
      background-color: rgba(244, 67, 54, 0.1);
    }
  }
</style>
