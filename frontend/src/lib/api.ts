/**
 * API client for interacting with the Whisper.cpp backend via Tauri commands
 */
import { invoke } from '@tauri-apps/api/core';

/**
 * Response from the recording commands
 */
interface RecordingResponse {
  success: boolean;
  file_path?: string;
  error?: string;
}

/**
 * Response from the transcription API
 */
export interface TranscriptionResponse {
  text: string;
  segments?: Array<{
    id: number;
    seek: number;
    start: number;
    end: number;
    text: string;
    tokens: number[];
    temperature: number;
    avg_logprob: number;
    compression_ratio: number;
    no_speech_prob: number;
  }>;
  success: boolean;
  error?: string;
}

/**
 * Check if the backend is running
 * This is a simplified check since we're using Tauri commands
 */
export async function checkBackendStatus(): Promise<{ status: string }> {
  try {
    // We'll just check if we can start the recorder
    // This doesn't actually start recording, just initializes the recorder
    const response = await invoke<RecordingResponse>('start_recording');
    return { status: response.success ? 'ready' : 'error' };
  } catch (error) {
    console.error('Error checking backend status:', error);
    return { status: 'error' };
  }
}

/**
 * Start recording audio using Tauri command
 */
export async function startRecording(): Promise<{ message: string; file?: string }> {
  try {
    const response = await invoke<RecordingResponse>('start_recording');

    if (response.success) {
      return {
        message: 'Recording started',
        file: response.file_path
      };
    } else {
      return {
        message: response.error || 'Failed to start recording'
      };
    }
  } catch (error) {
    console.error('Error starting recording:', error);
    return { message: `Failed to start recording: ${error}` };
  }
}

/**
 * Stop recording audio using Tauri command
 */
export async function stopRecording(): Promise<{ message: string; file?: string }> {
  try {
    const response = await invoke<RecordingResponse>('stop_recording');

    if (response.success) {
      return {
        message: 'Recording stopped',
        file: response.file_path
      };
    } else {
      return {
        message: response.error || 'Failed to stop recording'
      };
    }
  } catch (error) {
    console.error('Error stopping recording:', error);
    return { message: `Failed to stop recording: ${error}` };
  }
}

/**
 * Transcribe the recorded audio using Tauri command
 */
export async function transcribeAudio(): Promise<TranscriptionResponse> {
  try {
    const response = await invoke<TranscriptionResponse>('transcribe_audio');
    return response;
  } catch (error) {
    console.error('Error transcribing audio:', error);
    return {
      text: '',
      success: false,
      error: `Failed to transcribe audio: ${error}`,
    };
  }
}
