(setq word nil)
(defun search-voice ()
  (interactive)
  (let ()
    (setq word (if mark-active
           (buffer-substring-no-properties
            (region-beginning) (region-end))
         (current-word nil t)))
    (setq word (read-string
        (format "Search for (default %s): " word)
        nil nil word))
    (set-buffer (get-buffer-create "*schprc*"))
    (buffer-disable-undo)
    (erase-buffer)
    (let ((process
       (start-process-shell-command "schprc" "*schprc*" "search-word.bash" word )))
      (set-process-sentinel
       process
       (lambda (process sig) ;;must be 2 args
     (when (memq (process-status process) '(exit signal))
       (unless (string= (buffer-name) "*schprc*")
         (switch-to-buffer-other-window "*schprc*")
         (local-set-key (kbd "v") 'search-voice)
         (local-set-key (kbd "d") 'kid-sdcv-to-buffer)
         (local-set-key (kbd "C-n") 'forward-line)
         (local-set-key (kbd "q")
                (lambda ()
                  (interactive)
                  (bury-buffer)
                  (unless
                  (null (cdr (window-list))) ; only one window
                (delete-window))))
         (local-set-key (kbd "n")
                (lambda ()
                  (interactive) ;;demanded for key binding
                  (let (filename sttpos edtpos cmdbash
                         (line-end (line-end-position)))
                (save-excursion
                  (beginning-of-line)
                  (re-search-forward "\\(.+\\.lrc\\)[:-]\\[\\([0-9:]+\\)"
                             line-end t 1)
                  (setq filename (match-string 1))
                  (setq sttpos   (match-string 2))
                  (re-search-forward "\\[\\([0-9:]+\\)" line-end t 1)
                  (setq edtpos (match-string 1))
                  (setq cmdbash (concat "schprc.bash "
                            (shell-quote-argument filename)
                            " "
                            (shell-quote-argument sttpos)
                            " "
                            (shell-quote-argument edtpos)))
                  (message "playing ...  %s %s %s" filename sttpos edtpos)
                  (append-to-file (line-beginning-position)
                          (line-beginning-position 2)
                          "~/difficult-lines.txt")
                  (start-process-shell-command "voice" "*schprc*" cmdbash)))))
         (goto-char (point-min)))
       (goto-char (point-min))
       (while (search-forward word (point-max) t 1)
         (let (filename linend)
           (forward-line 0)
           (re-search-forward "\\(.+\\.lrc\\)\\([:-]\\[\\)" (line-end-position) t 1)
           (setq filename (match-string 1))
           (while (search-forward filename (line-end-position) t 1)
         (replace-match "")
         (delete-char 1))
           (forward-line)
           (setq linend (line-end-position))
           (if (search-forward filename linend t 1)
         (progn (re-search-forward "\\[[0-9:.]+\\]"  linend t 1)
         (end-of-line 0)
         (insert (match-string 0)))
         (end-of-line 0)
         (insert "[0.0]"))
))
       (goto-char (point-min))
       (while (< (point) (point-max))
         (if (search-forward word (line-end-position) t)
         (forward-line)
           (kill-line)
           (kill-line)
           ))
       (goto-char (point-min))
       ))))))